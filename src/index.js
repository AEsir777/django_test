import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'

function Square(props) {
    return (
        // JSX syntax
        // React.createElement('button', {prop}, {children})

        <button className="square" onClick={ props.onClick }>
            {props.value}
        </button>
    );
}

class Board extends React.Component { 
    renderSquare(i) {
        return React.createElement(Square, {
            value: this.props.squares[i],
            onClick: () => this.props.onClick(i)
        });
        /* (
            <Square
                value={this.state.squares[i]}
                onClick={() => this.handleClick(i)}
            />
        ); */
    }

    render() {
        return (
            <div>
                <div className="board-row">
                    {this.renderSquare(0)}
                    {this.renderSquare(1)}
                    {this.renderSquare(2)}
                </div>
                <div className="board-row">
                    {this.renderSquare(3)}
                    {this.renderSquare(4)}
                    {this.renderSquare(5)}
                </div>
                <div className="board-row">
                    {this.renderSquare(6)}
                    {this.renderSquare(7)}
                    {this.renderSquare(8)}
                </div>
            </div>
        );
    }
}

class Game extends React.Component {
    constructor(props) {
        super(props); 
        this.state = { 
            pastMoves: [{ squares: Array(9).fill(null) }],
            xNext: true,
            step: 0
        }
    }

    handleClick(i) {
        // create a copy of the squares array
        console.log('click');
        const pastMoves = this.state.pastMoves.slice(0, this.state.step + 1);
        const current = pastMoves[pastMoves.length - 1];
        const squares = current.squares.slice();
        if ( calculateWinner(squares) || squares[i] )
            return;

        squares[i] = this.state.xNext ? 'X' : 'O';
        this.setState({
            pastMoves: pastMoves.concat([{
                squares: squares
            }]),
            xNext: !this.state.xNext,
            step: pastMoves.length
        });
    }
    
    jumpTo(step) {
        this.setState({
            step: step,
            xIsNext: (step % 2) === 0
        })
    }

    render() {
        const pastMoves = this.state.pastMoves;
        const current = pastMoves[this.state.step];
        const winner = calculateWinner(current.squares);

        const moves = pastMoves.map((step, move) => {
            const description = move ? 'Go to move #' + move : 'Go to game start';
            return (
                <li key={move}>
                    <button onClick = {() => this.jumpTo(move)}>
                        {description}
                    </button>
                </li>
            )
        });


        let status;
        if ( winner )
            status = 'Winner: ' + winner;
        else
            status = 'Next player: ' + (this.props.xNext ? 'X' : 'O');


        return (
            <div className="game">
                <div className="game-board">
                    <Board
                        squares = {current.squares}
                        onClick = {(i) => this.handleClick(i)} 
                    />
                </div>
                <div className="game-info">
                    <div>{status}</div>
                    <ol>{moves}</ol>
                </div>
            </div>
        );
    }
}

// ========================================

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Game />);

function calculateWinner(squares) {
    const lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];
    for (let i = 0; i < lines.length; i++) {
        const [a, b, c] = lines[i];
        if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
            return squares[a];
        }
    }
    return null;
}
