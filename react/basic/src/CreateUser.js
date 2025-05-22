import React from 'react';

function CreateUser({ username, email, onChange, onCreate }) {
    return (
        <div>
            <input name="username" placeholder="계정명" value={username} onChange={onChange} />
            <input name="email" placeholder="email" value={email} onChange={onChange} />
            <button onClick={onCreate}>등록</button>
        </div>
    );
}

export default CreateUser;
