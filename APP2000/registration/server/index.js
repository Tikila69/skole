const mysql = require("mysql2")
const express = require("express")
const cors = require ("cors")
const app = express()

app.use(express.json())

app.use(cors({
    origin: ["http://localhost:3000"],
    methods: ["GET", "POST"],
    credentials: true
    })
)

const db = mysql.createConnection({
    user: "admin",
    host: "localhost",
    password: "admin",
    database: "userlogin"
})

app.post("/register", (req, res) => {
    const username = req.body.username
    const password = req.body.password

    db.execute(
        "INSERT INTO users (username, password) VALUES (?,?)",
        [username, password],
        (err, result) => {
            console.log(err)
        }
    )
})

app.post("/login", (req, res) => {
    const username = req.body.username
    const password = req.body.password
    
    db.execute(
        "SELECT * FROM users WHERE username=? AND password = ?",
        [username, password],
        (err, result) => {
            if (err) {
                res.send({err: err})
            }
            if (result.length>0) {
                res.send(result)
            } else {
                res.send({message: "Go fuck yourself"})
            }
        }
    )
})




app.listen(3001, () => {
    console.log("Smooth as a babys asshole")
})