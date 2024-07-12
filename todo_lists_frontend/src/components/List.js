import React from 'react';

class List extends React.Component {
  state = {
    title: 'ff',
    todos: [],
  };

  async fetchData(list_id) {
    try {
      let response = await fetch('http://localhost:8000/api/list/' + list_id)
      let data = await response.json()
      this.setState({
        title: data.title,
        todos: data.todos,
      })
    } catch (error) {
      console.log('Problem fetching list...');
      console.error(error);
    }
  }

  componentDidMount() {
    let { list_id } = this.props;
    this.fetchData(list_id);
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevProps.list_id !== this.props.list_id) {
      let { list_id } = this.props;
      this.fetchData(list_id)
    }
  }

  handleClick(todoDescription) {
    alert('You clicked on the todo: ' + todoDescription);
  }

  render() {
    return (
    <>
    <h1>{this.state.title}</h1>
    <ul>
      {this.state.todos.map((todo) =>
        <li onClick={() => this.handleClick(todo.description)} key={todo.id}>{todo.description}</li> 
      )}
    </ul>
    </>
    )
}
}

export default List;