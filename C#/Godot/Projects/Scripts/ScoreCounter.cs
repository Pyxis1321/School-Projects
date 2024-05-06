using Godot;

public partial class ScoreCounter : Label
{
    private int score = 0;

    // Called when the node enters the scene tree for the first time.
    public override void _Ready()
    {
        // Initialize label text with initial score
        UpdateScoreLabel();
    }

    // Update the score and display it on the label
    public void UpdateScore(int increment)
    {
        score += increment;
        UpdateScoreLabel();
    }

    // Reset the score to 0
    public void ResetScore()
    {
        score = 0;
        UpdateScoreLabel();
    }

    // Update the label text to display the current score
    private void UpdateScoreLabel()
    {
        Text = "Score: " + score;
    }
}