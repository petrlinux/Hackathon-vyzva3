using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using IronPython.Hosting;
using System.Threading;

public class Robot : MonoBehaviour
{
    public Vykresli supervisor;
    float elapsed = 0f;
    private int target;
    public int robot_id;
    public int start_point = 1000;
    private Thread _t1;
    bool _t1Paused = false;
    // Start is called before the first frame update
    void Start()
    {
        target = Random.Range(1, 600);
       // _t1 = new Thread(_func1);
       // _t1.Start();
    }

    // Update is called once per frame
    void Update()
    {
        elapsed += Time.deltaTime;
        if (elapsed >= 0.05f)
        {
            elapsed = elapsed % .05f;
            //_t1Paused = false;
            OutputTime();
        }
        //_t1Paused = true;
    }

    /*/private void _func1()
    {
        while(true)
        {
            while (_t1Paused) { }
            OutputTime();
        }
    }*/

    void OutputTime()
    {
        var engine = Python.CreateEngine();

        ICollection<string> searchPaths = engine.GetSearchPaths();

        //Path to the folder of greeter.py
        searchPaths.Add(@"C:\Assets\");
        //Path to the Python standard library
        searchPaths.Add(@"C:\Assets\Python\Lib");
        searchPaths.Add(@"C:\Assets\Python\Lib\site-packages\");
        engine.SetSearchPaths(searchPaths);

        dynamic py = engine.ExecuteFile(@"C:\Assets\Robot.py");
        string temp = "";
        for (int p = 0; p != 35 * 63; p++)
        {
            temp = temp + supervisor.pole[p].ToString() + ",";
        }
        dynamic obj = py.Pole(target, 63, temp, robot_id);
        string[] subs = obj.Split(',');
        for (int i = 0; i != 63 * 35; i++)
        {
            if (supervisor.pole[i] == robot_id)
                supervisor.pole[i] = 0;
        }
        supervisor.pole[int.Parse(subs[1]) * 63 + int.Parse(subs[0])] = robot_id;

        if (int.Parse(subs[2]) == 3)
        {
            if (target != start_point)
            {
                target = start_point;
                switch (robot_id)
                {
                    case 2000:
                        supervisor.is_full_0 = false;
                        break;
                    case 2001:
                        supervisor.is_full_1 = false;
                        break;
                    case 2002:
                        supervisor.is_full_2 = false;
                        break;
                    case 2003:
                        supervisor.is_full_3 = false;
                        break;
                    case 2004:
                        supervisor.is_full_4 = false;
                        break;
                }
            }  
            else
            {
                switch (robot_id)
                {
                    case 2000:
                        supervisor.is_full_0 = true;
                        break;
                    case 2001:
                        supervisor.is_full_1 = true;
                        break;
                    case 2002:
                        supervisor.is_full_2 = true;
                        break;
                    case 2003:
                        supervisor.is_full_3 = true;
                        break;
                    case 2004:
                        supervisor.is_full_4 = true;
                        break;
                }
                target = Random.Range(1, 600);
            }
                
        }

    }
    /*private void OnDestroy()
    {
        _t1.Abort();
    }*/


}
