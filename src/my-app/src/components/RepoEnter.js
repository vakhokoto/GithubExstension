import React from "react";
import Form from "react-bootstrap/Form";
import axios from "axios";

export class RepoEnter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { textInput: "" };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  handleSubmit(ev) {
    ev.preventDefault();
    axios
      .get("/token", {
        params: {
          token: "param",
        },
      })
      .then((response) => {
        console.log("response", response);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  handleChange(ev) {
    this.setState({ textInput: ev.target.value });
  }

  render() {
    return (
      <Form onSubmit={this.handleSubmit}>
        <Form.Group controlId="RepoInputter">
          <Form.Label>Enter Repo</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter Repository"
            value={this.state.textInput}
            onChange={this.handleChange}
          />
          {/* <Form.Text id="textInput" className="text-muted">
              We'll never share your token, trust us.
            </Form.Text> */}
        </Form.Group>
      </Form>
    );
  }
}
