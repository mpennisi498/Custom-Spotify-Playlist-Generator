import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import "bootstrap/dist/css/bootstrap.min.css";
import logo from "../../images/logo.png";

// This is the component that displays the navbar at the top of the page, the logo and title of the project
export default function MainNavbar() {
  return (
    <Navbar bg="dark" data-bs-theme="dark">
      <Container style={{ padding: "15px", marginLeft: "5px" }}>
        <img
          src={logo}
          width="50"
          height="50"
          style={{ display: "inline-block", marginRight: "10px" }}
          className="d-inline-block align-top"
          alt="Logo"
        />
        <Navbar.Brand href="home" style={{ fontSize: "30px" }}>
          Playlist Generator
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav"></Navbar.Collapse>
      </Container>
    </Navbar>
  );
}
