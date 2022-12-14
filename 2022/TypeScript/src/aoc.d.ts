declare module global {
    let appRoot: string;
    let inputRoot: string;
    let year: number;
}

declare interface Error {
    name: string
    message: string
    stack?: string
    code?: number | string
  }