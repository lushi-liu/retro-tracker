import { Inter } from 'next/font/google';
import Dashboard from '../components/Dashboard';

const inter = Inter({ subsets: ['latin'] });

export default function Home() {
  return (
    <main className={inter.className}>
    <h1>Retro Game Sentiment Tracker</h1>
    <Dashboard />
    </main>
  );
}