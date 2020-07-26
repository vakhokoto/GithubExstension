import React from "react";
import Form from "react-bootstrap/Form";
import axios from "axios";
import styled from "styled-components";

const Styles = styled.div`
  .inputGroup {
    position: relative;
  }
  .form-inline {
    width: 10%;
  }

  .form-group {
    width: 90%;
  }

  .input-group {
    width: 90% !important;
  }

  .form-control {
    width: 50% !important;
  }
`;

export class TokenInput extends React.Component {
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
        this.props.handler();
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
      <Styles>
        <Form onSubmit={this.handleSubmit}>
          <Form.Group controlId="TokenInputter">
            <Form.Label>Enter Token</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter Token"
              value={this.state.textInput}
              onChange={this.handleChange}
            />
            <Form.Text id="textInput" className="text-muted">
              We'll never share your token, trust us.
            </Form.Text>
          </Form.Group>
        </Form>
      </Styles>
    );
  }
}
