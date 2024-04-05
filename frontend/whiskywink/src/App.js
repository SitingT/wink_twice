import "./App.css";
import ShopCategory from "./Pages/ShopCategory";
import Navbar from "./Components/NavBar/NavBar";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginSignup from "./Pages/LoginSignup";
import Product from "./Pages/Product";
import Cart from "./Pages/Cart";
import SellItem from "./Pages/SellItem";
// import Shop from './Components/Pages/Shop';
import Footer from "./Components/Footer/Footer";
import Popular from "./Components/Popular/Popular";
import NewsLetter from "./Components/NewsLetter/NewsLetter";
import WhiskyForm from "./Components/WhiskyForm/WhiskyForm";
function App() {
  return (
    <div>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<ShopCategory category="all" />} />
          <Route
            path="/bourbon"
            element={<ShopCategory category="bourbon" />}
          />
          <Route path="/scotch" element={<ShopCategory category="scotch" />} />
          <Route
            path="/japanese"
            element={<ShopCategory category="japanese" />}
          />
          <Route path="/irish" element={<ShopCategory category="irish" />} />
          <Route path="/product" element={<Product />}>
            <Route path=":productId" element={<Product />} />
          </Route>
          <Route path="/cart" element={<Cart />} />
          <Route path="/login" element={<LoginSignup />} />
          <Route path="/Sell" element={<SellItem />} />
        </Routes>
        {/* <WhiskyForm /> */}

        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
