# The Devils in the Details CSCI 423 War-Trash Computer simulation

## War Details

**Objective:** Simulate the classic card game of "War."

### How to Play:

1. **Initialization:**
   - Shuffle the deck of cards.
   - Divide the deck evenly between two players.

2. **Turn Mechanics:**
   - Each player reveals their top card.
   - The player with the higher card value (Ace high) wins the turn and collects both cards.
   - In case of a tie, players continue drawing cards until one wins or a player runs out of cards.

3. **Running Out of Cards:**
   - If a player's hand is empty, they shuffle their winnings pile to form a new hand.

4. **Winning the Game:**
   - The player collecting all the cards is the winner.
   - In the rare event both players run out of cards during a tie, a coin is flipped to determine the winner.

### Gameplay Insights:
- The player with the most combined cards in their hand and winnings pile is leading the game.

---

## Trash Details

**Objective:** Clear out ten successive arrays of cards by matching card values to array slots (Ace low rules).

### Gameplay:

1. **Setup:**
   - The deck is shuffled.
   - Each player is dealt a 10-card array (cards face down).
   - One card is placed face-up in the discard pile, and the rest form the draw pile.

2. **Turn Mechanics:**
   - Players start their turn by picking a card from the draw pile or the discard pile.
   - They continue to play until they can't place any more cards.

3. **Card Placement:**
   - Players aim to match the value of cards in their hand to their respective positions in the array.
   - Jacks are wild and can be placed anywhere. Queens and Kings are always trash cards and can't be used in the array.

4. **Clearing Arrays and Winning:**
   - The game is won by the first player to clear 10 arrays of decreasing sizes (from 10 to 1).
   - Once an array is cleared, that player shuffles their cards and deals a new array, one card smaller than the last.
   - The player then continues their turn with the card in hand, without drawing a new one.

5. **Draw Pile Depletion:**
   - If the draw pile is empty at the start of a turn, the discard pile (excluding the top card) is reshuffled to form a new draw pile.

## Input:

| Argument | Description                                              |
|----------|----------------------------------------------------------|
| 1        | Game type: `war` or `trash`                              |
| 2        | Path to a file with Uniform(0,1) samples                 |


## Output:

The simulation should produce the following results:

- `N`: Total number of turns required to complete the game.
- `T`: Total number of winner transitions in the game.
- `L`: Point in the game when the last winner transition occurred, expressed as a fraction of `N`.

### Example Output:


