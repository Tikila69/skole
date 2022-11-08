import logo from '../logo.svg';

function Header() {
    return(
    <nav className="Nav">
        <img src={logo} className="Nav-logo" alt="Logo" />
        <ul className="Nav-links">
          <li>Pricing</li>
          <li>About</li>
          <li>Contact</li>
        </ul>
        </nav>
    )
};

export default Header;
