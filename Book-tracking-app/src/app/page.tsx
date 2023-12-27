import AddBook from '@/components/AddBook'
import Books from '@/components/Books'



export default function Home() {
  return (
    <main className="flex flex-col items-center justify-between p-24">
      <AddBook/>
      <Books/>
    </main>
  )
}
