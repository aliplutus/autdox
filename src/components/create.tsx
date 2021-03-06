import React from "react";
import lookup from "../api/api";

function Create(props: any) {
  const [state, setstate] = React.useState<any>({ title: "", description: "" });
  const callback = (response: any, status: number) => {
    props.setData((pre: any) => {
      return [...pre, response.books];
    });
    console.log(response, status);
  };
  return (
    <div>
      <input
        onChange={(e) =>
          setstate((pre: any) => {
            return { ...pre, title: e.target.value };
          })
        }
        placeholder="title"
      />
      <input
        onChange={(e) =>
          setstate((pre: any) => {
            return { ...pre, description: e.target.value };
          })
        }
        placeholder="description"
      />
      <input
        required={false}
        onChange={(e) =>
          setstate((pre: any) => {
            return {
              ...pre,
              who_can_see: e.target.value,
            };
          })
        }
        placeholder="who_can_see"
      />
      <button
        onClick={() => {
          console.log(state);
          lookup("POST", "api/addbook/", callback, {
            author: 1,
            ...state,
          });
        }}
      >
        create book
      </button>
    </div>
  );
}

export default Create;
