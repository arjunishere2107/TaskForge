import { useEffect, useState } from "react";
import API from "../api/api";
import { Link } from "react-router-dom";

function Dashboard() {

  const [tasks, setTasks] = useState([]);
  const [role, setRole] = useState("member");

  useEffect(() => {

    fetchTasks();

    const userRole = localStorage.getItem("role");

    if (userRole) {
      setRole(userRole);
    }

  }, []);

  const fetchTasks = async () => {

    try {

      const res = await API.get("/tasks/");

      setTasks(res.data);

    } catch (error) {

      console.log(error);

    }
  };

  const completed = tasks.filter(
    (task) => task.status === "done"
  ).length;

  const pending = tasks.filter(
    (task) => task.status !== "done"
  ).length;

  return (

    <div className="min-h-screen bg-gray-100 flex">

      {/* Sidebar */}
      <div className="w-64 bg-gray-900 text-white p-5">

        <h1 className="text-3xl font-bold mb-8">
          TaskForge
        </h1>

        <ul className="space-y-4">

          <li className="bg-gray-800 p-3 rounded-lg">
            Dashboard
          </li>

          {
            role === "admin" && (
              <li>
                <Link
                  to="/create-task"
                  className="block bg-blue-600 p-3 rounded-lg"
                >
                  Create Task
                </Link>
              </li>
            )
          }

          {
            role === "admin" && (
              <li className="bg-gray-800 p-3 rounded-lg">
                Manage Team
              </li>
            )
          }

          <li
            onClick={() => {
              localStorage.clear();
              window.location.href = "/login";
            }}
            className="bg-red-500 p-3 rounded-lg cursor-pointer"
          >
            Logout
          </li>

        </ul>

      </div>

      {/* Main Content */}
      <div className="flex-1 p-6">

        <div className="flex justify-between items-center mb-6">

          <div>

            <h2 className="text-3xl font-bold">
              Welcome {role === "admin" ? "Admin" : "Member"}
            </h2>

            <p className="text-gray-500">
              Team Task Management Dashboard
            </p>

          </div>

          <div className="bg-white px-4 py-2 rounded-xl shadow">
            Role: {role}
          </div>

        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-5 mb-8">

          <div className="bg-white p-5 rounded-2xl shadow">

            <h3 className="text-gray-500">
              Total Tasks
            </h3>

            <p className="text-4xl font-bold mt-2">
              {tasks.length}
            </p>

          </div>

          <div className="bg-white p-5 rounded-2xl shadow">

            <h3 className="text-gray-500">
              Completed
            </h3>

            <p className="text-4xl font-bold text-green-600 mt-2">
              {completed}
            </p>

          </div>

          <div className="bg-white p-5 rounded-2xl shadow">

            <h3 className="text-gray-500">
              Pending
            </h3>

            <p className="text-4xl font-bold text-orange-500 mt-2">
              {pending}
            </p>

          </div>

        </div>

        {/* Tasks */}
        <div>

          <h2 className="text-2xl font-bold mb-4">
            Project Tasks
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">

            {
              tasks.map((task) => (

                <div
                  key={task.id}
                  className="bg-white p-5 rounded-2xl shadow"
                >

                  <div className="flex justify-between items-center mb-3">

                    <h3 className="text-xl font-bold">
                      {task.title}
                    </h3>

                    <span
                      className={`px-3 py-1 rounded-full text-white text-sm ${
                        task.status === "done"
                          ? "bg-green-500"
                          : "bg-orange-500"
                      }`}
                    >
                      {task.status}
                    </span>

                  </div>

                  <p className="text-gray-600 mb-4">
                    {task.description}
                  </p>

                  <div className="text-sm text-gray-500">
                    Assigned To: {task.assigned_to}
                  </div>

                </div>

              ))
            }

          </div>

        </div>

      </div>

    </div>

  );
}

export default Dashboard;