import React from "react";
import { TokenInput } from "./components/TokenInput";
import { RepoEnter } from "./components/RepoEnter.js";

export default function handleToken() {}

export class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = { isLoggedIn: true, repoEntered: false };
  }

  tokenHandler() {
    this.setState({ isLoggedIn: true });
  }

  render() {
    return (
      <React.Fragment>
        <h5>Go-to GitHub and get personal access token:</h5>
        <h5>Here is the link</h5>
        <a href="https://github.com/settings/tokens">
          <h5>Click Me</h5>
        </a>
        <div>
          <h5>Paste it below:</h5>
        </div>
        {this.state.isLoggedIn ? (
          <TokenInput handler={this.tokenHandler} />
        ) : (
          <RepoEnter></RepoEnter>
        )}
      </React.Fragment>
    );
  }
}
