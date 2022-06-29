<template>
	<div style="paddin: 10px;margin-left: 20px;height: 50px;margin-top: 20px;font-size: 15px;font-weight: bold;">
		<div style="display: flex;justify-content: space-between;">
			<div>
				<h2 style="color: #1989fa;">
						SQL生成工具
				</h2>
			</div>
			<div style="line-height: 75px;">
				<router-link to="/"><span style="color: #1989fa;">插入语句</span> </router-link>&nbsp;&nbsp;&nbsp;&nbsp;
				<router-link to="/createtable" style="color: #1989fa;"><span>创表语句</span></router-link>&nbsp;&nbsp;&nbsp;&nbsp;
				<router-link to="/sql"><span style="color: #1989fa;">sql执行</span></router-link>&nbsp;&nbsp;&nbsp;&nbsp;
				<router-link to="/submitsql"><span style="color: #1989fa;">sql文件上传</span></router-link>&nbsp;&nbsp;&nbsp;&nbsp;
			</div>
		</div>

		<hr/>
	</div>
</template>

<script>
</script>

<style>
</style>
