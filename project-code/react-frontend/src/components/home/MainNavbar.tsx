import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css'
import logo from '../../images/logo.png'



export default function MainNavbar() {
    return (
      <Navbar bg="dark" data-bs-theme="dark" >
      <Container style={{padding:"15px", marginLeft:"5px"}} >
        <img
          src={logo}
          width="50"
          height="50"
          style={{display: "inline-block", marginRight: "10px"}}
          className="d-inline-block align-top"
          alt="Logo"
        />
        <Navbar.Brand href="home" style={{fontSize:"30px"}}>Playlist Generator</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav>
            <Nav.Link href="home" style={{color:"#1bd760", fontSize:"20px"}}>Home</Nav.Link>
            <Nav.Link href="about" style={{color:"#1bd760",fontSize:"20px"}} >About</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    );
}
