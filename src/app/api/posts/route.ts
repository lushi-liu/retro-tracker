import { connectToDatabase } from "../../../lib/mongodb";
import { NextResponse } from "next/server";

export async function GET() {
  try {
    const { db } = await connectToDatabase();
    const posts = await db
      .collection("posts")
      .find({ sentiment: { $exists: true } })
      .toArray();
    return NextResponse.json(posts);
  } catch (error) {
    return NextResponse.json(
      { error: "Failed to fetch posts" },
      { status: 500 }
    );
  }
}
