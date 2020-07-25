import React from "react";
import { TokenInput } from "./components/TokenInput";
// import { Guide } from "./components/Guide";
import { Link } from "react-router-dom";

export const Home = () => (
  <React.Fragment>
    <h3>Go-to GitHub and get personal access token:</h3>
    <h3>Here is the link</h3>
    <a href="https://github.com/settings/tokens">
      <h5>Click Me</h5>
    </a>
    <div>
      <h5>Paste it below:</h5>
    </div>
    <TokenInput></TokenInput>
  </React.Fragment>
);
