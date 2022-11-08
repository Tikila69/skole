import './App.css';
import Contacts from "./Contacts"
import Data from "./Data"


function App() {
  const cards = Data.map(item => {
    return (
      <Contacts
        id={item.id}
        img={item.img}
        name={item.name}
        phone={item.phone}
        email={item.email}
      />
    )
  })

  return (
    <div className="App">
      <div className="contacts">
          {cards}
      </div>
      
    </div>
  );
}

export default App;
