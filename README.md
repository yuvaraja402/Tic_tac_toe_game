# TicTacToe with randomGenerator AI

Tic-tac-toe (also known as noughts and crosses or Xs and Os) is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

# Posting Quick link's here:

### Python Script :

URL : https://github.com/yuvaraja402/Tic_tac_toe_game_with-random_AI/blob/master/tictactoe_1D_list.py




<figure>
  <figcaption>Your code title</figcaption>
  <pre>
    <code class="language-javascript">
    
        i1 = [-1,-2,0,1,2,3,9]
        i2 = [-1,-3]
        i3 = [1,2,3]
        def positive(input):
            #getting +ve and -ve numbers
            #pos = [i for i in input if i > 0]
            #neg = [i for i in input if i < 0]
            ans = []
            for i in range(1,max(input)+1):
                if i in input:
                    continue
                else:
                    ans.append(i)
            if len(ans) > 0:
                ans = min(ans)
            if len(ans) == 0:
                ans.append(1)
            return ans
        answer = positive(i2)
        print('\n',i1)
        print('\n',answer)
        
    </code>
  </pre>
</figure>
