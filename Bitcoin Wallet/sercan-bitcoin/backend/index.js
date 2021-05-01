const express = require('express')
require('./db/mongoose')
const userRouter = require('./routes/userRoute.')


const cors = require('cors')
const app = express()
const port = process.env.PORT || 5000


app.use(express.json())
app.use(cors());

app.use(userRouter)


app.listen(port, ()=>{
    console.log(`server listening on localhost : ${port}`)
})