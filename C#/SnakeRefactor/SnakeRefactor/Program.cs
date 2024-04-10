class GameObject
{
	public int Xpos { get; set; }
	public int Ypos { get; set; }
}

class Snake : GameObject
{
	public ConsoleColor SnakeColor { get; set; }

	public void Move(Direction direction)
	{
		switch (direction)
		{
			case Direction.Up: Ypos--; break;
			case Direction.Down: Ypos++; break;
			case Direction.Left: Xpos--; break;
			case Direction.Right: Xpos++; break;
		}
	}
}

class Berry : GameObject
{
}

enum Direction
{
	Up,
	Down,
	Left,
	Right
}

namespace SnakeGame
{
	class Program
	{
		private static int windowHeight = 16;
		private static int windowWidth = 32;
		private static int initialSnakeSize = 5;
		private static Snake snake;
		private static Berry berry;
		private static List<int> xPos = new List<int>();
		private static List<int> yPos = new List<int>();
		private static int score;
		private static bool gameOver;
		private static Direction movement = Direction.Right;
		private static Random randNum = new Random();

		static void Main(string[] args)
		{
			InitializeGame();
			while (!gameOver)
			{
				UpdateGame();
				RenderGame();
				Thread.Sleep(100);
			}
			EndGame();
		}

		static void InitializeGame()
		{
			Console.CursorVisible = false;
			Console.SetWindowSize(windowWidth, windowHeight);
			DrawBorders();
			score = initialSnakeSize;
			gameOver = false;

			snake = new Snake
			{
				Xpos = Console.WindowWidth / 2,
				Ypos = Console.WindowHeight / 2,
				SnakeColor = ConsoleColor.Red
			};

			berry = new Berry
			{
				Xpos = randNum.Next(1, windowWidth - 1),
				Ypos = randNum.Next(1, windowHeight - 1),
			};
		}

		static void UpdateGame()
		{
			UpdateDirection();
			snake.Move(movement);

			// Check for self collision
			for (int i = 0; i < xPos.Count; i++)
			{
				if (xPos[i] == snake.Xpos && yPos[i] == snake.Ypos)
				{
					gameOver = true;
					return;
				}
			}

			// Check for border collision
			if (snake.Xpos == 0 || snake.Xpos == windowWidth - 1 || snake.Ypos == 0 || snake.Ypos == windowHeight - 1)
			{
				gameOver = true;
				return;
			}

			// Check for berry collection
			if (snake.Xpos == berry.Xpos && snake.Ypos == berry.Ypos)
			{
				score++;
				berry.Xpos = randNum.Next(1, windowWidth - 1);
				berry.Ypos = randNum.Next(1, windowHeight - 1);
			}

			xPos.Add(snake.Xpos);
			yPos.Add(snake.Ypos);

			// Ensure the tail moves with the snake, maintaining length
			if (xPos.Count > score)
			{
				xPos.RemoveAt(0);
				yPos.RemoveAt(0);
			}
		}

		static void RenderGame()
		{
			// Redraw only head and erase tail as needed
			Console.ForegroundColor = snake.SnakeColor;
			if (xPos.Count > 1)
			{
				var tail = new { X = xPos[0], Y = yPos[0] };
				Console.SetCursorPosition(tail.X, tail.Y);
				Console.Write(" ");
			}

			var head = new { X = xPos.Last(), Y = yPos.Last() };
			Console.SetCursorPosition(head.X, head.Y);
			Console.Write("■");

			// Redraw berry
			Console.ForegroundColor = ConsoleColor.Cyan;
			Console.SetCursorPosition(berry.Xpos, berry.Ypos);
			Console.Write("■");
		}

		static void EndGame()
		{
			Console.SetCursorPosition(0, windowHeight / 2);
			Console.ForegroundColor = ConsoleColor.Red;
			Console.WriteLine("Game over, Score: " + (score - initialSnakeSize));
			Console.ReadKey(true);
		}

		static void UpdateDirection()
		{
			if (Console.KeyAvailable)
			{
				ConsoleKeyInfo key = Console.ReadKey(true);
				switch (key.Key)
				{
					case ConsoleKey.UpArrow when movement != Direction.Down:
						movement = Direction.Up;
						break;
					case ConsoleKey.DownArrow when movement != Direction.Up:
						movement = Direction.Down;
						break;
					case ConsoleKey.LeftArrow when movement != Direction.Right:
						movement = Direction.Left;
						break;
					case ConsoleKey.RightArrow when movement != Direction.Left:
						movement = Direction.Right;
						break;
				}
			}
		}

		static void DrawBorders()
		{
			Console.ForegroundColor = ConsoleColor.White;
			for (int x = 0; x < windowWidth; x++)
			{
				Console.SetCursorPosition(x, 0);
				Console.Write("■");
				Console.SetCursorPosition(x, windowHeight - 1);
				Console.Write("■");
			}
			for (int y = 0; y < windowHeight; y++)
			{
				Console.SetCursorPosition(0, y);
				Console.Write("■");
				Console.SetCursorPosition(windowWidth - 1, y);
				Console.Write("■");
			}
		}
	}
}
