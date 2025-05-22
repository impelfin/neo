import React, { useRef, useState } from 'react';
import UserList from './UserList';
import CreateUser from './CreateUser';

function App() {
    const [inputs, setInputs] = useState({
        username: '',
        email: '',
    });

    const { username, email } = inputs;

    const onChange = e => {
        const { name, value } = e.target;
        setInputs({
            ...inputs,
            [name]: value,
        });
    };

    const [users, setUsers] = useState([
        { id: 1, username: 'developer', email: 'public.developer@gmail.com' },
        { id: 2, username: 'tester', email: 'public.tester@gmail.com' },
        { id: 3, username: 'moon', email: 'public.moon@gmail.com' },
    ]);

    const nextId = useRef(4);
    const onCreate = () => {
        const user = {
            id: nextId.current,
            username,
            email,
        };
        setUsers([...users, user]);

        setInputs({
            username: '',
            email: '',
        });
        nextId.current += 1;
    };
    return (
        <>
            <CreateUser username={username} email={email} onChange={onChange} onCreate={onCreate} />
            <UserList users={users} />
        </>
    );
}

export default App;
