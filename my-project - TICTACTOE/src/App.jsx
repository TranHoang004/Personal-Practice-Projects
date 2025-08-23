import { useState } from "react";

export default function App() {
  const [board, setBoard] = useState(Array(9).fill(null)); // 9 ô
  const [isXNext, setIsXNext] = useState(true); // true = X, false = O

  // Hàm kiểm tra thắng
  const calculateWinner = (squares) => {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8], // ngang
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8], // dọc
      [0, 4, 8],
      [2, 4, 6], // chéo
    ];
    for (let [a, b, c] of lines) {
      if (
        squares[a] &&
        squares[a] === squares[b] &&
        squares[a] === squares[c]
      ) {
        return squares[a];
      }
    }
    return null;
  };

  const winner = calculateWinner(board);

  const handleClick = (index) => {
    if (board[index] || winner) return; // đã đánh rồi hoặc đã có người thắng
    const newBoard = [...board];
    newBoard[index] = isXNext ? "X" : "O";
    setBoard(newBoard);
    setIsXNext(!isXNext);
  };

  const resetGame = () => {
    setBoard(Array(9).fill(null));
    setIsXNext(true);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-5xl font-extrabold mb-8 text-gray-800 drop-shadow-lg">
        Tic Tac Toe 🎮
      </h1>

      <div className="grid grid-cols-3 gap-4 sm:gap-6 mt-8">
        {board.map((cell, index) => (
          <button
            key={index}
            className="w-24 h-24 sm:w-28 sm:h-28 md:w-32 md:h-32 
                 text-4xl sm:text-5xl md:text-6xl font-bold 
                 flex items-center justify-center 
                 border-2 border-gray-600 bg-gray-800 hover:bg-gray-700 
                 rounded-lg shadow-md transition"
            onClick={() => handleClick(index)}
          >
            {cell}
          </button>
        ))}
      </div>

      <p className="mt-4 text-xl">
        {winner
          ? `🎉 Người thắng: ${winner}`
          : `Lượt tiếp theo: ${isXNext ? "X" : "O"}`}
      </p>
      <button
        onClick={resetGame}
        className="mt-6 px-6 py-3 text-lg font-semibold bg-blue-600 text-white rounded-xl shadow-lg hover:bg-blue-700 transition"
      >
        Chơi lại
      </button>
    </div>
  );
}
