import { Book, Status } from '@/types'
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

const backendUrl = process.env.REACT_APP_BACKEND_API_URL ?? 'http://localhost:8000'
console.log("backend",backendUrl)
export const webApi = createApi({
  reducerPath: 'webApi',
  baseQuery: fetchBaseQuery({ baseUrl: backendUrl}),
  tagTypes:["Books"],
  endpoints: (builder) => ({ 
    getBooks: builder.query<Book[], void>({
        query: () => '/books',
        providesTags:['Books']
    }),
    updateBook: builder.mutation<void, { id:string, status:Status }>({
        query: ({id, status}) => ({
            url:`books/${id}?book_status=${status}`,
            method:'PUT'
        }),
        invalidatesTags:['Books']

    }),
    addBook: builder.mutation<void, string>({
        query: (title) => ({
            url:'books',    
            method:'POST',
            body:{title:title}
        }),
        invalidatesTags:['Books']

    }),
    deleteBook: builder.mutation<void, string>({
        query: (id) => ({
            url:`books/${id}`,
            method:'DELETE'
        }),
        invalidatesTags:['Books']

    }),
  }),
})


export const { 
    useGetBooksQuery, 
    useUpdateBookMutation, 
    useAddBookMutation, 
    useDeleteBookMutation
 } = webApi