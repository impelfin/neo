import React from 'react';

function Hello({name, color, isSpectial }) {
    return (
        <div style={{color}}>{ isSpectial && <b>*</b>}
        Hello~ {name}
        </div>
    );
}

Hello.defaultProps = {
    name: 'NoName',
}

export default Hello;