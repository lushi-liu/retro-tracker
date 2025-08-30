import { Schema, model, models } from 'mongoose';

const PostSchema = new Schema({
    game: { type: String, required: true },
    text: { type: String, required: true },
    sentiment: { type: String, enum: ['positive', 'negative', 'neutral'] },
    score: { type: Number }, // Sentiment score
    timestamp: { type: Date, default: Date.now },
});

export const Post = models.Post || model('Post', PostSchema);