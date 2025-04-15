import React from 'react'
import logo from './logo.svg';
import './App.css';
import CompoundForm from './CompoundForm';


// // JSX is syntatic sugar of some react methods

function App() {
  const reactElement = <h1>Hello from JSX!</h1>
  return (
    <div className="App">
      <header className="App-header">
        <h1>MyNestEgg Calculator</h1>
        <CompoundForm />
        {/* <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      </header>
    </div>
  );
}

export default App;
