'use client'

import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { ChangeEvent, useState } from "react"
import { useAddBookMutation } from "@/store/api"
import { ToastAction } from "@/components/ui/toast"
import { useToast } from "@/components/ui/use-toast"
import ClipLoader from "react-spinners/ClipLoader";

type Props = {}

const AddBook = (props: Props) => {
    const [ addBook, { isLoading }] = useAddBookMutation()
    const [ title, setTitle ] = useState('')
    const { toast } = useToast()
    const handleClick = async () => {
        console.log('jdf')
        try {
            await addBook(title).unwrap()
            setTitle('')
        } catch (error) {
            toast({
                variant: "destructive",
                title: "Uh oh! Something went wrong.",
                description: "Failed to add book.",
                action: <ToastAction altText="Try again">Try again</ToastAction>,
              })
        }
    }
    const handleChange = (e: ChangeEvent<HTMLInputElement>) => { 
        setTitle(e.target.value)
    }
    console.log(isLoading)
  return (
    <div className='flex gap-3 items-center px-1'>
        <Input value={title} onChange={(e) => handleChange(e)} className="w-[70vw] lg:w-[50vw] " />
        <Button disabled={isLoading} onClick={handleClick}>{isLoading ? <ClipLoader loading={isLoading} />:'Add Book'}</Button>
    </div>
  )
}

export default AddBook