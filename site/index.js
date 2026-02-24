import express from "express";
import bodyParser from "body-parser";
import { MongoClient } from "mongodb";

dotenv.config();

const uri = process.env.URI;
const client = new MongoClient(uri);

async function run() {

}
run().catch(console.dir);

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));
app.set("view engine", "ejs");
app.set("views", "./views");



app.get("/", async (req, res) => {

    await client.connect();
    const db = client.db("catalogo");
    const collection = db.collection("jogos");
    const resultado = await collection.find({}).toArray();
    // console.log(resultado.length)
    let result_games;
    const jogos = [];
    for (let i = 0; i < resultado.length; i++) {
        result_games = {
            "title": resultado[i]["titulo"],
            "url": resultado[i]["url"],
            "text": resultado[i]["texto"]
        };
        jogos.push(result_games)
    };
    console.log(jogos)

    res.render("index.ejs", { resultado: jogos })
});

app.listen(3000, () => {
    console.log("server rodando em http://localhost:3000")
});