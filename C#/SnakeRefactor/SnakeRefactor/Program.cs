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
		protected static int windowHeight = 16;
		protected static int windowWidth = 32;
		protected static int initialSnakeSize = 5;

		private static readonly Random randNum = new Random();
		private static Direction movement = Direction.Right;

		static void DrawBorders()
		{
			Console.ForegroundColor = ConsoleColor.White;
			for (int x = 0; x < Console.WindowWidth; x++)
			{
				Console.SetCursorPosition(x, 0);
				Console.Write("■");
				Console.SetCursorPosition(x, Console.WindowHeight - 1);
				Console.Write("■");
			}
			for (int y = 0; y < Console.WindowHeight; y++)
			{
				Console.SetCursorPosition(0, y);
				Console.Write("■");
				Console.SetCursorPosition(Console.WindowWidth - 1, y);
				Console.Write("■");
			}
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

		static void Main(string[] args)
		{
			Console.CursorVisible = false;
			Console.SetWindowSize(windowWidth, windowHeight);
			DrawBorders();
	
			int score = initialSnakeSize;
			bool gameOver = false;

			List<int> xPos = new List<int>();
			List<int> yPos = new List<int>();

			Snake snake = new Snake
			{
				Xpos = Console.WindowWidth / 2,
				Ypos = Console.WindowHeight / 2,
				SnakeColor = ConsoleColor.Red
			};

			Berry berry = new Berry
			{
				Xpos = randNum.Next(1, windowWidth - 1),
				Ypos = randNum.Next(1, windowHeight - 1),
			};

			while (!gameOver)
			{
				UpdateDirection();
				snake.Move(movement);

				// Check for self collision
				for (int i = 0; i < xPos.Count; i++)
				{
					if (xPos[i] == snake.Xpos && yPos[i] == snake.Ypos)
					{
						gameOver = true;
						break;
					}
				}

				// Check for border collision
				if (snake.Xpos == Console.WindowWidth - 1 || snake.Xpos == 0 || snake.Ypos == Console.WindowHeight - 1 || snake.Ypos == 0)
				{
					gameOver = true;
				}

				if (snake.Xpos == berry.Xpos && snake.Ypos == berry.Ypos)
				{
					score++;
					berry.Xpos = randNum.Next(1, windowWidth - 1);
					berry.Ypos = randNum.Next(1, windowHeight - 1);
				}
				else if (xPos.Count >= score)
				{
					var tailX = xPos[0];
					var tailY = yPos[0];
					Console.SetCursorPosition(tailX, tailY);
					Console.Write(" ");
					xPos.RemoveAt(0);
					yPos.RemoveAt(0);
				}

				xPos.Add(snake.Xpos);
				yPos.Add(snake.Ypos);

				Console.ForegroundColor = snake.SnakeColor;
				foreach (var pos in xPos.Zip(yPos, (x, y) => new { X = x, Y = y }))
				{
					Console.SetCursorPosition(pos.X, pos.Y);
					Console.Write("■");
				}

				Console.ForegroundColor = ConsoleColor.Cyan;
				Console.SetCursorPosition(berry.Xpos, berry.Ypos);
				Console.Write("■");

				Thread.Sleep(100);
			}

			Console.SetCursorPosition(0, Console.WindowHeight / 2);
			Console.ForegroundColor = ConsoleColor.Red;
			Console.WriteLine("Game over, Score: " + (score - initialSnakeSize));
			Console.ReadKey(true);
		}
	}
}