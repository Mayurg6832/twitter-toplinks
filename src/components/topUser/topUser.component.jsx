import React, { Component } from "react";

class AllUser extends Component {
  constructor() {
    super();
    this.state = {
      users: null,
    };
  }
  componentDidMount() {
    const apiUrl = "https://toplink-mayur.herokuapp.com/api/top_user";
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => this.setState({ users: data }));
  }

  render() {
    console.log(this.state.users);
    return (
      <>
        <h2>Top User who shared most links</h2>
        {this.state.users ? (
          <>
            {this.state.users.map(({ user_name }) => (
              <p>{user_name}</p>
            ))}
          </>
        ) : (
          <h3>Wow! such empty</h3>
        )}
      </>
    );
  }
}

export default AllUser;
