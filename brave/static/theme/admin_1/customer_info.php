<?php require "dbconnect.php"; ?>
<!DOCTYPE HTML>
<meta charset="UTF_8">   
<html> 
<head>
        <!--<meta charset="utf-8" />
        <title>Metronic Admin Theme #1 | Responsive Bootstrap Tables</title>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta content="width=device-width, initial-scale=1" name="viewport" />
        <meta content="Preview page of Metronic Admin Theme #1 for responsive bootstrap table demos" name="description" />
        <meta content="" name="author" />
        <!-- BEGIN GLOBAL MANDATORY STYLES -->
        <!--<link href="http://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700&amp;subset=all" rel="stylesheet" type="text/css" />
        <link href="http://keenthemes.com/preview/metronic/theme/assets/global/plugins/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css" />
        <link href="http://keenthemes.com/preview/metronic/theme/assets/global/plugins/simple-line-icons/simple-line-icons.min.css" rel="stylesheet" type="text/css" />
        <link href="http://keenthemes.com/preview/metronic/theme/assets/global/plugins/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
        <link href="http://keenthemes.com/preview/metronic/theme/assets/global/plugins/bootstrap-switch/css/bootstrap-switch.min.css" rel="stylesheet" type="text/css" />
        <!-- END GLOBAL MANDATORY STYLES -->
        <!-- BEGIN THEME GLOBAL STYLES -->
        <!--<link href="http://keenthemes.com/preview/metronic/theme/assets/global/css/components.min.css" rel="stylesheet" id="style_components" type="text/css" />
        <link href="http://keenthemes.com/preview/metronic/theme/assets/global/css/plugins.min.css" rel="stylesheet" type="text/css" />
        <!-- END THEME GLOBAL STYLES -->
        <!-- BEGIN THEME LAYOUT STYLES -->
        <!--<link href="http://keenthemes.com/preview/metronic/theme/assets/layouts/layout/css/layout.min.css" rel="stylesheet" type="text/css" />
        <link href="http://keenthemes.com/preview/metronic/theme/assets/layouts/layout/css/themes/darkblue.min.css" rel="stylesheet" type="text/css" id="style_color" />
        <link href="http://keenthemes.com/preview/metronic/theme/assets/layouts/layout/css/custom.min.css" rel="stylesheet" type="text/css" />
        <!-- END THEME LAYOUT STYLES -->
        <!--<link rel="shortcut icon" href="http://keenthemes.com/preview/metronic/theme/admin_1/favicon.ico" /> --></head>
<body>              
 <?php
         $sql="SELECT * FROM customer_info";
	     $result=mysql_query($sql);
	     $count=mysql_affected_rows();
	        if($count>0)
	           {
				   $_SESSION['c_email'] = $_POST['c_email'];
				    while($row = mysql_fetch_array($result))
	                  {
		                $l=$row['fname'];
		                $m=$row['lname'];
						$t=$row['tel'];
						$f=$row['streetaddress'];
						$r=$row['city'];
						$s=$row['state'];
						$ll=$row['user_id'];
					  ?>   
					   <div class="row">
                            <div class="col-md-12">
                                <!-- BEGIN SAMPLE TABLE PORTLET-->
                                <div class="portlet box green">
                                    <div class="portlet-title">
                                        <div class="caption">
                                            <i class="fa fa-cogs"></i>User Information Table</div>
                                        <div class="tools">
                                            <a href="javascript:;" class="collapse"> </a>
                                            <a href="#portlet-config" data-toggle="modal" class="config"> </a>
                                            <a href="javascript:;" class="reload"> </a>
                                            <a href="javascript:;" class="remove"> </a>
                                        </div>
                                    </div>
                                    <div class="portlet-body flip-scroll">
                                        <table class="table table-bordered table-striped table-condensed flip-content">
                                            <thead class="flip-content">
                                                <tr>
                                                    <th width="20%">First Name </th>
                                                    <th> Last Name </th>
                                                    <th class="numeric"> Phone Number</th>
                                                    <th  > Street Address </th>
                                                    <th  > City </th>
                                                    <th  > State </th>
                                                    <th  > User_id </th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr>
                                                    <td> <?php echo l;?></td>
                                                    <td> <?php echo m;?> </td>
                                                    <td class="numeric"> <?php echo t;?></td>
                                                    <td class="numeric"> <?php echo f;?> </td>
                                                    <td class="numeric"> <?php echo r;?> </td>
                                                    <td class="numeric"> <?php echo s;?></td>
                                                    <td class="numeric"><?php echo ll;?> </td>>
                                                </tr>
												<?php }?> 
                                            </tbody>
                                        </table>
                                    </div>
                                </div></div>
</body>
</html>