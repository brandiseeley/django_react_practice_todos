import React, { useState } from 'react';
import Lists from './components/Lists';
import List from './components/List';
import './App.css';

// import ListSummary from './components/ListSummary';

function App() {
  let [selectedListId, setSelectedListId] = useState(1);

  let handleListClick = (listId) => {
    console.log('Changing list id...');
    console.log('Current is: ', selectedListId);
    console.log('Trying to set it to: ', listId);
    setSelectedListId(listId);
    console.log('After setting is: ', selectedListId);
  }

  return (
    <>
      <Lists onSelectList={handleListClick}/>
      <List list_id={selectedListId}/>
    </>
  )
}

export default App;
