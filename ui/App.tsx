import React from 'react'

const App: React.FC = () => {
  const name = "React User"

  const unusedVariable = 42   // This will trigger @typescript-eslint/no-unused-vars
  console.log("Hello world")  // This may trigger debug-statements hook

  return (
    <div className="app-container">
      <h1>Hello, {name}</h1>
    </div>
  )
}

export default App
