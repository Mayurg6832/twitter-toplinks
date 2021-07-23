import HomePage from "./pages/homepage.component";
import AllUser from "./components/topUser/topUser.component";
import TopDomain from "./components/top-domain/top-domain.component";
import Links from "./components/nav/nav.component";
import { Switch, Route } from "react-router-dom";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Links />
      <Switch>
        <Route exact path="/" component={HomePage} />
        <Route exact path="/top-user" component={AllUser} />
        <Route exact path="/top-domain" component={TopDomain} />
      </Switch>
    </div>
  );
}

export default App;
