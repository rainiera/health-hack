//
//  HomeViewController.swift
//  HealthCruncher
//
//  Created by Shaun Mataire on 7/25/15.
//  Copyright (c) 2015 HealthCruncher. All rights reserved.
//

import UIKit

class HomeViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        //set app design
        var nav = self.navigationController?.navigationBar
        nav?.barStyle = UIBarStyle.BlackTranslucent
        nav?.titleTextAttributes  = [NSForegroundColorAttributeName: UIColor.whiteColor()]
        nav?.tintColor = UIColor.whiteColor()
        
     
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}


//Universal input Values
var zipCodeText: String!
var nameText: String!
var ageText: String!
var weightText: String!
var heightText: String!
var sexText: String!
var raceText: String!
