import React from 'react';

class Lists extends React.Component {
  state = {
    lists: []
  };

  async componentDidMount() {
    try {
      let response = await fetch('http://localhost:8000/api/lists');
      let data = await response.json();
      this.setState({ lists: data });
    } catch (error) {
      console.log('Problem fetching lists...');
      console.error(error);
    }
  }

  handleClick(list_id) {
    this.props.onSelectList(list_id);
  }

  render() {
    return (
    <>
    <h1>All Todo Lists</h1>
    <ul>
      {this.state.lists.map((list) =>
        <li onClick={() => this.handleClick(list.id)} key={list.id}>{list.title}</li> 
      )}
    </ul>
    </>
    )
}
}

export default Lists;