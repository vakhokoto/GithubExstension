import React from "react";
import Container from "react-bootstrap/Container";
import styled from "styled-components";

const Styles = styled.div`
  .container {
    backgroundcolor: "blue";
  }
`;

export const Layout = (props) => (
  <Styles>
    <Container>{props.children}</Container>
  </Styles>
);
