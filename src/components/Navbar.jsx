import { Link } from "react-router-dom";

function Navbar() {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "flex-end",
        padding: "20px",
        borderBottom: "1px solid lightgray"
      }}
    >
      <Link to="/evaluation">
        <button>Vai alla valutazione</button>
      </Link>
    </div>
  );
}

export default Navbar;