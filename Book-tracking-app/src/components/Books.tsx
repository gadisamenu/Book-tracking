'use client'
import {
    Card,
    CardContent,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card"
import { Button } from "./ui/button"
import { Book, Status } from "@/types"
import { MdDelete } from "react-icons/md";
import { useDeleteBookMutation, useGetBooksQuery, useUpdateBookMutation } from "@/store/api"
import ClipLoader from "react-spinners/ClipLoader";
import { useToast } from "@/components/ui/use-toast"
import { ToastAction } from "@/components/ui/toast"

type Props = {}


const Books = (props: Props) => {
    const { data:books, isLoading } = useGetBooksQuery()

  return (
    <div className='grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 w-[90vw] pt-10'>
        <div>
            <div className="text-xl font-bold px-5">To Read</div>
            {books &&
                books.filter(book => book.status === 'to-read').map((book, index) => 
                    <Book key={index} book={book}/>
                )
            }
        </div>
        <div>
            <div className="text-xl font-bold px-5">In Progress</div>
            {books &&
                books.filter(book => book.status === 'in-progress').map((book, index) => 
                    <Book key={index} book={book}/>
                )
            }
        </div>
        <div>
            <div className="text-xl font-bold px-5">Completed</div>
            {books &&
                books.filter(book => book.status === 'complete').map((book, index) => 
                    <Book key={index} book={book}/>
                )
            }
        </div>
    </div>
  )
}

export default Books




type BookProps = {
    book:Book
}

const Book = ({book}: BookProps) => {
    const [ updateBook, { isLoading:updating } ] = useUpdateBookMutation()
    const [ deleteBook, { isLoading:deleting } ] = useDeleteBookMutation()
    const { toast } = useToast()

    const handleClick = async () => {
        let newStatus:Status;
        if(book.status === 'to-read'){
            newStatus = 'in-progress'
        }else if (book.status === 'in-progress'){
            newStatus = 'complete'
        }else{
            newStatus = 'in-progress'
        }
        try {
            await updateBook({ id:book.id, status:newStatus}).unwrap()
        } catch (error) {
            console.log(error)
            toast({
                variant: "destructive",
                title: "Uh oh! Something went wrong.",
                description: "There was a problem with your request.",
                action: <ToastAction altText="Try again">Try again</ToastAction>,
              })
        }
    }
    const handleDelete = async () => {
        try {
            await deleteBook(book.id).unwrap()
        } catch (error) {
            toast({
                variant: "destructive",
                title: "Uh oh! Something went wrong.",
                description: "Failed to delete book",
                action: <ToastAction altText="Try again">Try again</ToastAction>,
              })
        }
    }
  return (
    <Card className="m-2">
        <CardHeader className="flex flex-row justify-between">
            <CardTitle>{book.title}</CardTitle>
            <Button disabled={deleting} size="icon" variant={'ghost'} onClick={handleDelete}>
                {deleting ?  <ClipLoader loading={deleting} />:<MdDelete size={30}/>}
            </Button>
        </CardHeader>
        <CardContent>
          <Button disabled={updating} onClick={handleClick}>{
          updating ?  <ClipLoader loading={updating} />:(book.status === 'to-read' ? 'Read':book.status === 'in-progress' ? 'Complete':'Reread')
          }
          </Button>
        </CardContent>
    </Card>

  )
}
