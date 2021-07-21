import React, { Component } from "react";
import OutlinedCard from "../tweet/tweet.component";

class Directory extends Component {
  constructor() {
    super();
    this.state = {
      tweets: null,
    };
  }
  componentDidMount() {
    const apiUrl = "http://127.0.0.1:8000/api/all_tweets";
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => this.setState({ tweets: data }));
  }

  render() {
    console.log(this.state.tweets);
    return (
      <>
        <h2>Actual Tweets containing links</h2>
        {this.state.tweets ? (
          <>
            {this.state.tweets.map(({ tweet_id, ...otherProps }) => (
              <OutlinedCard key={tweet_id} {...otherProps} />
            ))}
          </>
        ) : (
          <h3>Wow! such empty</h3>
        )}
      </>
    );
  }
}

export default Directory;
