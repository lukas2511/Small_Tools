<?php


$con=new SQLite3("library.db");

function errorr(){
	global $con;
	echo "Known Groups:\n";
	$groups=$con->query("select group_name from groups");
	while($group=$groups->fetchArray()){
		echo " - ".$group['group_name']."\n";
	}
	die();
}

if(!isset($_SERVER['argv'][1])) errorr();
$groupname=$_SERVER['argv'][1];
$export_to="../Export/".$groupname;

$gid=$con->query("select groupid from groups where group_name = '".$groupname."'");
errorr();
$gid=$gid->fetchArray();
errorr();
$gid=$gid['groupid'];
errorr();

$group=$con->query("select * from person_groups where groupid = ".$gid);

if(!is_dir($export_to)) mkdir($export_to,777,true);

while($person=$group->fetchArray()){
	$pid=$person['personid'];
	$person=$con->query("select * from persons where personid = ".$pid)->fetchArray();
	$faces=$con->query("select * from faces where personid = ".$pid);
	$pname=trim($person['first_name']." ".$person['last_name']);
	if(!is_dir($export_to."/faces/".$pname)) mkdir($export_to."/faces/".$pname,777,true);
	while($face=$faces->fetchArray()){
		$iid=$face['imageid'];
		echo "Person: ".$pname." (".$pid."), Image: ".$iid."\n";
		$image=$con->query("select * from image_files where imageid = ".$iid)->fetchArray();
		if($image){
			$picture = new Imagick("../".$image['file_path']);
			$picture->cropImage($face['bbox_w'],$face['bbox_h'],$face['bbox_x']-($face['bbox_w']/2),$face['bbox_y']-($face['bbox_h']/2));
			$picture->writeImage($export_to."/faces/".$pname."/".strtr($image['file_path'],array("/"=>"_")));
			copy("../".$image['file_path'],$export_to."/".$pname."/".strtr($image['file_path'],array("/"=>"_")));
		}
	}
}

?>
