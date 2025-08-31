"use client";

import { useState, useEffect } from "react";
import { Line } from "react-chartjs-2";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

interface Post {
  _id: string;
  game: string;
  text: string;
  sentiment: "positive" | "negative" | "neutral";
  score: number;
  timestamp: string;
}

const Dashboard = () => {
  const [posts, setPosts] = useState<Post[]>([]);

  useEffect(() => {
    fetch("/api/posts")
      .then((res) => res.json())
      .then((data) => setPosts(data))
      .catch((err) => console.error("Error fetching posts:", err));
  }, []);

  const chartData = {
    labels: posts.map((p) =>
      p.timestamp ? new Date(p.timestamp).toLocaleDateString() : ""
    ),
    datasets: [
      {
        label: "Sentiment Score",
        data: posts.map((p) => p.score ?? 0),
        borderColor: "#3dc050ff",
        fill: false,
      },
    ],
  };

  return (
    <div>
      <h2>Game Sentiment Trends</h2>
      {posts.length === 0 ? (
        <p>No posts yet.</p>
      ) : (
        <>
          <Line data={chartData} />
          {posts.map((post) => (
            <div key={post._id}>
              <h3>{post.game}</h3>
              <p>
                Sentiment: {post.sentiment} (Score: {post.score})
              </p>
            </div>
          ))}
        </>
      )}
    </div>
  );
};

export default Dashboard;
