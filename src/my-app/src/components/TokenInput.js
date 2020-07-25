import React from "react";
import InputGroup from "react-bootstrap/InputGroup";
import FormContro from "react-bootstrap/FormControl";
import Form from "react-bootstrap/Form";

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

function handleSubmit() {
  console.log("bla");
}

export const TokenInput = () => (
  <Styles>
    <Form>
      <Form.Group controlId="TokenInputter">
        <Form.Label>Enter Token</Form.Label>
        <Form.Control type="text" placeholder="Enter the token" />
        <Form.Text className="text-muted">
          We'll never share your token, trust us.
        </Form.Text>
      </Form.Group>
    </Form>
  </Styles>
);
