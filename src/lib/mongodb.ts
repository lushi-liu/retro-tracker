import { MongoClient } from 'mongodb';

const uri = process.env.MONGODB_URI || 'mongodb://localhost:27017/retro-sentiment';
const client = new MongoClient(uri);

export async function connectToDatabase() {
    try {
        await client.connect();
        const db = client.db('retro-sentiment');
        return { db, client };
    } catch (error) {
        console.error('MongoDB connection error:', error);
        throw error;
    }
}