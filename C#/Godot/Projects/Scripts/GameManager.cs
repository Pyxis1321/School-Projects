using Godot;
using System;
using System.Collections.Generic;

public partial class GameManager : Node
{
    public float speed { get; set; } = 0.6F;
    private int segmentSize = 128;
    private Vector2 gameArea = new Vector2(1664, 1664);
    private Vector2 startingPoss;
    private double passedTime;
    private Vector2 direction;
    private List<Sprite2D> snakeSegments = new List<Sprite2D>();
    private Node2D food;
    private bool isGameOver = false;
    private ScoreCounter scoreCounter;
    public override void _Ready()
    {
        var initialSnakeSegment = GetNode<Sprite2D>("Snake");
        food = GetNode<Node2D>("Food");
        scoreCounter = GetNode<ScoreCounter>("ScoreCounter");
        snakeSegments.Add(initialSnakeSegment);
        direction = Vector2.Right;
        startingPoss = initialSnakeSegment.Position;
        SpawnFood();
    }

    public override void _Process(double delta)
    {
        if (!isGameOver)
        {
            Vector2 inputDirection = UpdateDirection();
            if (inputDirection != Vector2.Zero) direction = inputDirection;

            passedTime += delta;
            if (passedTime >= speed)
            {
                MoveSnake();
                passedTime = 0;
                CheckSelfCollision();
            }

            CheckBounds();
            CheckFoodCollision();
        }
        else if (Input.IsKeyPressed(Key.R))
        {
            RestartGame();
        }
    }

    private void RestartGame()
{
    // Disable and reset positions rather than freeing and recreating
    foreach (var segment in snakeSegments)
    {
        segment.Visible = false;  // Hide instead of freeing
        segment.Position = startingPoss;  // Reset position
    }
    snakeSegments.Clear();  // Clear the list

    // Re-enable the initial segment and ensure it's visible
    var initialSnakeSegment = GetNode<Sprite2D>("Snake");
    initialSnakeSegment.Position = startingPoss;
    initialSnakeSegment.Visible = true;
    snakeSegments.Add(initialSnakeSegment);

    SpawnFood();
    isGameOver = false;
}

    private void EndGame()
    {
        isGameOver = true;
        scoreCounter.ResetScore();
    }

    private Vector2 UpdateDirection()
    {
        if (Input.IsKeyPressed(Key.Left) && direction != Vector2.Right)
        {
            return Vector2.Left;
        }
        else if (Input.IsKeyPressed(Key.Right) && direction != Vector2.Left)
        {
            return Vector2.Right;
        }
        else if (Input.IsKeyPressed(Key.Up) && direction != Vector2.Down)
        {
            return Vector2.Up;
        }
        else if (Input.IsKeyPressed(Key.Down) && direction != Vector2.Up)
        {
            return Vector2.Down;
        }
        else
        {
            return direction;
        }
    }

    private void MoveSnake()
    {
        Vector2 previousPosition = snakeSegments[0].Position;
        snakeSegments[0].Position += (direction * segmentSize);
        for (int i = 1; i < snakeSegments.Count; i++)
        {
            Vector2 temp = snakeSegments[i].Position;
            snakeSegments[i].Position = previousPosition;
            previousPosition = temp;
        }
    }

    private void CheckSelfCollision()
    {
        
        Rect2 headRect = new Rect2(snakeSegments[0].Position - new Vector2(segmentSize / 2, segmentSize / 2), new Vector2(segmentSize, segmentSize));
        for (int i = 1; i < snakeSegments.Count; i++)
        {
            Rect2 bodyRect = new Rect2(snakeSegments[i].Position - new Vector2(segmentSize / 2, segmentSize / 2), new Vector2(segmentSize, segmentSize));
            if (headRect.Intersects(bodyRect))
            {
                EndGame();
                break;
            }
        }
    }

    private void CheckFoodCollision()
    {
        Rect2 snakeRect = new Rect2(snakeSegments[0].Position - new Vector2(segmentSize / 2, segmentSize / 2), new Vector2(segmentSize, segmentSize));
        Rect2 foodRect = new Rect2(food.Position, new Vector2(64, 64));

        if (snakeRect.Intersects(foodRect))
        {
            SpawnFood();
            IncreaseSnakeLength();
            
            scoreCounter.UpdateScore(1);
        }
    }

    private void IncreaseSnakeLength()
    {
        var newSegment = new Sprite2D();
        newSegment.Texture = snakeSegments[0].Texture; // Assuming all segments use the same texture
        newSegment.Position = snakeSegments[snakeSegments.Count - 1].Position;
        AddChild(newSegment);
        snakeSegments.Add(newSegment);
    }

    private void SpawnFood()
    {
        Random random = new Random();
        int gridSize = 20;
        int foodX = random.Next(0, (int)(gameArea.X / gridSize)) * gridSize;
        int foodY = random.Next(0, (int)(gameArea.Y / gridSize)) * gridSize;
        food.Position = new Vector2(foodX, foodY);
    }

    private void CheckBounds()
    {
        if (snakeSegments[0].Position.X < 0 || snakeSegments[0].Position.X > gameArea.X || snakeSegments[0].Position.Y < 0 || snakeSegments[0].Position.Y > gameArea.Y)
        {
            EndGame();
        }
    }
}
