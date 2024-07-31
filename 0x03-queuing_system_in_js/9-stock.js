import express from 'express';
import { createClient } from 'redis';

// Server
const app = express();
const PORT = 1245;


// Data
const listProducts = [
    {
        id: 1,
        name: "Suitcase 250",
        price: 50,
        stock: 4
    }, 
    {
        id: 2,
        name: "Suitcase 450",
        price: 100,
        stock: 10
    }, 
    {
        id: 3,
        name: "Suitcase 650",
        price: 350,
        stock: 2
    }, 
    {
        id: 4,
        name: "Suitcase 1050",
        price: 550,
        stock: 5
    }
]

// Data access
function getItemById(id) {
    return listProducts.find((item) => item.id === id);
}

// Products
app.get('/list_products', (req, res) => {
    res.json(listProducts.map((item) => {
        return {
            itemId: item.id,
            itemName: item.name,
            price: item.price,
            initialAvailableQuantity: item.stock
        }
    }));
})

// In stock in Redis
const client = createClient({
    socket: {
      host: '127.0.0.1',
      port: 6379,
    }
})
  .on('error', (err) => console.log('Redis client not connected to the server: ', err))
  .on('connect', () => console.log('Redis client connected to the server'));
    
client.connect();

async function reverseStockById(itemId, stock) {
    await client.set(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
    try{
        const result = await client.get(itemId);
        return result;
    } catch (err) {
        console.log(err);
    }
}

// Product Detail
app.get('/list_products/:itemId', async (req, res) => {
    const itemId = req.params.itemId;
    const item = getItemById(Number(itemId));
    if (item) {
        const reserved = await getCurrentReservedStockById(itemId);
        res.json({
            itemId: item.id,
            itemName: item.name,
            price: item.price,
            initialAvailableQuantity: item.stock,
            currentQuantity: item.stock - (reserved ? Number(reserved) : 0)
        })
    } else {
        res.json({status: "Product not found"})
    }
})

// Reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = req.params.itemId;
    const item = await getItemById(Number(itemId));
    if (!item) res.json({"status":"Product not found"});
    else {
        if (item.stock - (await getCurrentReservedStockById(itemId) || 0)) {
            const reserved = await getCurrentReservedStockById(itemId);
            reverseStockById(itemId, (reserved ? Number(reserved) : 0) + 1);
            res.json({status:"Reservation confirmed", itemId: itemId});
        } else {
            res.json({status: "Not enough stock available", itemId: itemId});
        }
    }
})

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));