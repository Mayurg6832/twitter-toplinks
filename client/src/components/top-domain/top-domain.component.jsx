import React, { Component } from "react";

class TopDomain extends Component {
  constructor() {
    super();
    this.state = {
      domain: null,
    };
  }
  componentDidMount() {
    const apiUrl = "http://127.0.0.1:8000/api/top_domain";
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => this.setState({ domain: data }));
  }

  render() {
    console.log(this.state.domain);
    return (
      <>
        <h2>List of Top Domains that have been shared so far</h2>
        {this.state.domain ? (
          <>
            {this.state.domain.map(({ domain_name }) => (
              <p>
                <a href={domain_name}>{domain_name}</a>
              </p>
            ))}
          </>
        ) : (
          <h3>Wow! such empty</h3>
        )}
      </>
    );
  }
}

export default TopDomain;
