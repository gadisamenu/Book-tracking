export interface Book {
    id:string, 
    title:string, 
    status:Status
}

export type Status =  'to-read' | 'in-progress' | 'complete'