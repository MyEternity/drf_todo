import './App.css';
import React from "react";
import UserList from "./components/users";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        };
    };

    componentDidMount() {
        const users = [
            {
                'username': 'admin',
                'first_name': 'test',
                'last_name': 'test',
                'email': 'test@mail.local'
            },
            {
                'username': 'demo',
                'first_name': 'demo',
                'last_name': 'test',
                'email': 'demo@mail.loc'
            }
        ]
        this.setState(
            {
                'users': users
            }
        )
    }

    render() {
        return (
            <div>
                <UserList users={this.state.users}/>
            </div>
        );
    };
};

export default App;
